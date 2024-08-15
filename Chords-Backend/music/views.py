from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user_auth.models import User
from music.models import (
    AllMusic, 
    SeasonalCollectionSongs, 
    ContactUs, 
    Contribute, 
    Support, 
    NewSong, 
    CreatePlayList, 
    SeasonalCollectionsList,
    BeginnerFriendlyCollectionsList,
    BeginnerFriendlyCollectionSongs,
    SearchCollections,
    SearchCollectionsSongs,
    TrendingSongs,
    DiscoverNewSongs,
    TopArtistList,
    ArtistSongs,
    ArtistProfile,
)
 
from music.serializers import (
    AllMusicSerializer,
    SeasonalCollectionSerializer,
    ContactUsSerializer,
    ContributeSerializer,
    SupportSerializer,
    NewSongSerializer,
    PlayListSerializer,
    SeasonalCollectionsListSerializer,
    BeginnerFriendlyCollectionsListSerializer,
    BeginnerFriendlyCollectionsSongsSerializer,
    SearchCollectionsSerializer,
    SearchCollectionsSongsSerializer,
    TrendingSongsSerializer,
    DiscoverSongsSerializer,
    TopArtistListSerializer,
    ArtistSongsSerializer,
    ArtistProfileSerializer,
)
from pyfcm import FCMNotification
import uuid

class MusicViewset(viewsets.ModelViewSet):
    queryset = AllMusic.objects.all()
    serializer_class = AllMusicSerializer
    http_method_names = ['get', 'post', 'retrieve', 'put', 'patch']


class AllMusicView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = AllMusic.objects.all()
        serializer = AllMusicSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"Musics": serializer.data}}, status=200)

    def post(self, request):
        try:
            serializer = AllMusicSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Music created successfully!!!', 'data': {'music': serializer.data}}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)  # Print validation errors
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            music = get_object_or_404(AllMusic, pk=pk)
            serializer = AllMusicSerializer(music, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Music updated successfully!!!', 'data': {'music': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            music = get_object_or_404(AllMusic, pk=pk)
            serializer = AllMusicSerializer(music, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Music partially updated successfully!!!', 'data': {'music': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            music = get_object_or_404(AllMusic, pk=pk)
            music.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Music deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SeasonalCollectionsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = SeasonalCollectionsList.objects.all()
        serializer = SeasonalCollectionsListSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"seasonal_collections": serializer.data}}, status=200)

    def post(self, request):
        try:
            serializer = SeasonalCollectionsListSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection created successfully!!!', 'data': {'seasonal_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            seasonal_collection = get_object_or_404(SeasonalCollectionsList, pk=pk)
            serializer = SeasonalCollectionsListSerializer(seasonal_collection, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection updated successfully!!!', 'data': {'seasonal_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            seasonal_collection = get_object_or_404(SeasonalCollectionsList, pk=pk)
            serializer = SeasonalCollectionsListSerializer(seasonal_collection, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection partially updated successfully!!!', 'data': {'seasonal_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            seasonal_collection = get_object_or_404(SeasonalCollectionsList, pk=pk)
            seasonal_collection.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Similar methods can be added to other view classes following the pattern above. For example, here are the updates for `SeasonalCollectioSongsView`, `BeginnerFriendlyCollectionsListView`, `SearchCollectionsView`, and `TrendingSongsView`.

class SeasonalCollectioSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = SeasonalCollectionSongs.objects.all()
        serializers = SeasonalCollectionSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"session_collections": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = SeasonalCollectionSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Session Collection created successfully!!!', 'data': {'session_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            seasonal_collection_song = get_object_or_404(SeasonalCollectionSongs, pk=pk)
            serializer = SeasonalCollectionSerializer(seasonal_collection_song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection Song updated successfully!!!', 'data': {'seasonal_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            seasonal_collection_song = get_object_or_404(SeasonalCollectionSongs, pk=pk)
            serializer = SeasonalCollectionSerializer(seasonal_collection_song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection Song partially updated successfully!!!', 'data': {'seasonal_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            seasonal_collection_song = get_object_or_404(SeasonalCollectionSongs, pk=pk)
            seasonal_collection_song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Seasonal Collection Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BeginnerFriendlyCollectionsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = BeginnerFriendlyCollectionsList.objects.all()
        serializers = BeginnerFriendlyCollectionsListSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"beginner_friendly_collections": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = BeginnerFriendlyCollectionsListSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection created successfully!!!', 'data': {'beginner_friendly_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            beginner_friendly_collection = get_object_or_404(BeginnerFriendlyCollectionsList, pk=pk)
            serializer = BeginnerFriendlyCollectionsListSerializer(beginner_friendly_collection, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection updated successfully!!!', 'data': {'beginner_friendly_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            beginner_friendly_collection = get_object_or_404(BeginnerFriendlyCollectionsList, pk=pk)
            serializer = BeginnerFriendlyCollectionsListSerializer(beginner_friendly_collection, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection partially updated successfully!!!', 'data': {'beginner_friendly_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            beginner_friendly_collection = get_object_or_404(BeginnerFriendlyCollectionsList, pk=pk)
            beginner_friendly_collection.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchCollectionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = SearchCollections.objects.all()
        serializers = SearchCollectionsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"search_collections": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = SearchCollectionsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection created successfully!!!', 'data': {'search_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            search_collection = get_object_or_404(SearchCollections, pk=pk)
            serializer = SearchCollectionsSerializer(search_collection, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection updated successfully!!!', 'data': {'search_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            search_collection = get_object_or_404(SearchCollections, pk=pk)
            serializer = SearchCollectionsSerializer(search_collection, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection partially updated successfully!!!', 'data': {'search_collection': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            search_collection = get_object_or_404(SearchCollections, pk=pk)
            search_collection.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Search Collection deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchCollectionsSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = SearchCollectionsSongs.objects.all()
        serializers = SearchCollectionsSongsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"search_collection_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = SearchCollectionsSongsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection Song created successfully!!!', 'data': {'search_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            song = get_object_or_404(SearchCollectionsSongs, pk=pk)
            serializer = SearchCollectionsSongsSerializer(song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection Song updated successfully!!!', 'data': {'search_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            song = get_object_or_404(SearchCollectionsSongs, pk=pk)
            serializer = SearchCollectionsSongsSerializer(song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Search Collection Song partially updated successfully!!!', 'data': {'search_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            song = get_object_or_404(SearchCollectionsSongs, pk=pk)
            song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Search Collection Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BeginnerFriendlyCollectionsSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = BeginnerFriendlyCollectionSongs.objects.all()
        serializers = BeginnerFriendlyCollectionsSongsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"beginner_friendly_collection_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = BeginnerFriendlyCollectionsSongsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection Song created successfully!!!', 'data': {'beginner_friendly_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            song = get_object_or_404(BeginnerFriendlyCollectionSongs, pk=pk)
            serializer = BeginnerFriendlyCollectionsSongsSerializer(song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection Song updated successfully!!!', 'data': {'beginner_friendly_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            song = get_object_or_404(BeginnerFriendlyCollectionSongs, pk=pk)
            serializer = BeginnerFriendlyCollectionsSongsSerializer(song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection Song partially updated successfully!!!', 'data': {'beginner_friendly_collection_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            song = get_object_or_404(BeginnerFriendlyCollectionSongs, pk=pk)
            song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Beginner Friendly Collection Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TrendingSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = TrendingSongs.objects.all()
        serializers = TrendingSongsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"trending_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = TrendingSongsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Trending Song created successfully!!!', 'data': {'trending_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            trending_song = get_object_or_404(TrendingSongs, pk=pk)
            serializer = TrendingSongsSerializer(trending_song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Trending Song updated successfully!!!', 'data': {'trending_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            trending_song = get_object_or_404(TrendingSongs, pk=pk)
            serializer = TrendingSongsSerializer(trending_song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Trending Song partially updated successfully!!!', 'data': {'trending_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            trending_song = get_object_or_404(TrendingSongs, pk=pk)
            trending_song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Trending Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DiscoveredSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = DiscoverNewSongs.objects.all()
        serializers = DiscoverSongsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"discovered_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = DiscoverSongsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Discovered Song created successfully!!!', 'data': {'discovered_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            discovered_song = get_object_or_404(DiscoverNewSongs, pk=pk)
            serializer = DiscoverSongsSerializer(discovered_song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Discovered Song updated successfully!!!', 'data': {'discovered_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            discovered_song = get_object_or_404(DiscoverNewSongs, pk=pk)
            serializer = DiscoverSongsSerializer(discovered_song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Discovered Song partially updated successfully!!!', 'data': {'discovered_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            discovered_song = get_object_or_404(DiscoverNewSongs, pk=pk)
            discovered_song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Discovered Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TopArtistsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = TopArtistList.objects.all()
        serializers = TopArtistListSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"top_artists": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = TopArtistListSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Top Artist created successfully!!!', 'data': {'top_artist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            top_artist = get_object_or_404(TopArtistList, pk=pk)
            serializer = TopArtistListSerializer(top_artist, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Top Artist updated successfully!!!', 'data': {'top_artist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            top_artist = get_object_or_404(TopArtistList, pk=pk)
            serializer = TopArtistListSerializer(top_artist, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Top Artist partially updated successfully!!!', 'data': {'top_artist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            top_artist = get_object_or_404(TopArtistList, pk=pk)
            top_artist.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Top Artist deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ArtistSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = ArtistSongs.objects.all()
        serializers = ArtistSongsSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"artist_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = ArtistSongsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Song created successfully!!!', 'data': {'artist_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            artist_song = get_object_or_404(ArtistSongs, pk=pk)
            serializer = ArtistSongsSerializer(artist_song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Song updated successfully!!!', 'data': {'artist_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            artist_song = get_object_or_404(ArtistSongs, pk=pk)
            serializer = ArtistSongsSerializer(artist_song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Song partially updated successfully!!!', 'data': {'artist_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            artist_song = get_object_or_404(ArtistSongs, pk=pk)
            artist_song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Artist Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ArtistProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = ArtistProfile.objects.all()
        serializers = ArtistProfileSerializer(result, many=True)
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"artist_profiles": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = ArtistProfileSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Profile created successfully!!!', 'data': {'artist_profile': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            artist_profile = get_object_or_404(ArtistProfile, pk=pk)
            serializer = ArtistProfileSerializer(artist_profile, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Profile updated successfully!!!', 'data': {'artist_profile': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            artist_profile = get_object_or_404(ArtistProfile, pk=pk)
            serializer = ArtistProfileSerializer(artist_profile, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Artist Profile partially updated successfully!!!', 'data': {'artist_profile': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            artist_profile = get_object_or_404(ArtistProfile, pk=pk)
            artist_profile.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Artist Profile deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ContactUsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve a list of all contact messages.
        """
        result = ContactUs.objects.all()
        serializer = ContactUsSerializer(result, many=True, context={'request': request})
        return Response({
            'status': True,
            'status_code': '200',
            'message': '',
            'data': {'contacts': serializer.data}
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new contact message.
        """
        try:
            serializer = ContactUsSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'status_code': '200',
                    'message': 'Your message has been sent successfully!!!',
                    'data': {'contact_us': serializer.data}
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': False,
                    'status_code': '400',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'status_code': '500',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        """
        Update an existing contact message by ID.
        """
        try:
            contact = get_object_or_404(ContactUs, pk=pk)
            serializer = ContactUsSerializer(contact, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'status_code': '200',
                    'message': 'Contact Us entry updated successfully!!!',
                    'data': {'contact_us': serializer.data}
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': False,
                    'status_code': '400',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'status_code': '500',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        """
        Partially update an existing contact message by ID.
        """
        try:
            contact = get_object_or_404(ContactUs, pk=pk)
            serializer = ContactUsSerializer(contact, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'status_code': '200',
                    'message': 'Contact Us entry partially updated successfully!!!',
                    'data': {'contact_us': serializer.data}
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': False,
                    'status_code': '400',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'status_code': '500',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        """
        Delete an existing contact message by ID.
        """
        try:
            contact = get_object_or_404(ContactUs, pk=pk)
            contact.delete()
            return Response({
                'status': True,
                'status_code': '200',
                'message': 'Contact Us entry deleted successfully!!!'
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                'status': False,
                'status_code': '500',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContributionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = Contribute.objects.all()
        serializers =  ContributeSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"contributions": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = ContributeSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Contribution made successfully!!!', 'data': {'contribution': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            contribution = get_object_or_404(Contribute, pk=pk)
            serializer = ContributeSerializer(contribution, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Contribution updated successfully!!!', 'data': {'contribution': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            contribution = get_object_or_404(Contribute, pk=pk)
            serializer = ContributeSerializer(contribution, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Contribution partially updated successfully!!!', 'data': {'contribution': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            contribution = get_object_or_404(Contribute, pk=pk)
            contribution.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Contribution deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SupportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = Support.objects.all()
        serializers = SupportSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"supports": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = SupportSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Support created successfully!!!', 'data': {'support': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            support = get_object_or_404(Support, pk=pk)
            serializer = SupportSerializer(support, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Support updated successfully!!!', 'data': {'support': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            support = get_object_or_404(Support, pk=pk)
            serializer = SupportSerializer(support, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Support partially updated successfully!!!', 'data': {'support': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            support = get_object_or_404(Support, pk=pk)
            support.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Support deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class NewSongView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = NewSong.objects.all()
        serializers = NewSongSerializer(result, many=True, context={'request': request})
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"new_songs": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = NewSongSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'New Song created successfully!!!', 'data': {'new_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            new_song = get_object_or_404(NewSong, pk=pk)
            serializer = NewSongSerializer(new_song, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'New Song updated successfully!!!', 'data': {'new_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            new_song = get_object_or_404(NewSong, pk=pk)
            serializer = NewSongSerializer(new_song, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'New Song partially updated successfully!!!', 'data': {'new_song': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            new_song = get_object_or_404(NewSong, pk=pk)
            new_song.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'New Song deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class PlayListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = CreatePlayList.objects.all()
        serializers = PlayListSerializer(result, many=True)
        return Response({'status': True, 'status_code': '200', 'message': '', "data": {"playlists": serializers.data}}, status=200)

    def post(self, request):
        try:
            serializer = PlayListSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Playlist created successfully!!!', 'data': {'playlist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            playlist = get_object_or_404(CreatePlayList, pk=pk)
            serializer = PlayListSerializer(playlist, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Playlist updated successfully!!!', 'data': {'playlist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            playlist = get_object_or_404(CreatePlayList, pk=pk)
            serializer = PlayListSerializer(playlist, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'status_code': '200', 'message': 'Playlist partially updated successfully!!!', 'data': {'playlist': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": False, 'status_code': '400', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            playlist = get_object_or_404(CreatePlayList, pk=pk)
            playlist.delete()
            return Response({'status': True, 'status_code': '200', 'message': 'Playlist deleted successfully!!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, 'status_code': '500', "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)